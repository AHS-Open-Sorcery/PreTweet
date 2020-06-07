import dayjs from 'dayjs';
import store, { Store, error, Post } from './store';
import * as http from './rest';

type Transformer = (store: Store) => Store;
type IO = () => Promise<any>;
const IONothing: IO = () => Promise.resolve();
type Effect = {
    io?: IO,
    transform?: Transformer
};

function updatePost(id: number, updater: (posts: Post[], index: number) => any) {
    store.update(s => {
        const i = s.posts.findIndex(it => it.id === id);
        console.assert(i !== -1);
        updater(s.posts, i);
        return s;
    });
}

export const ACTIONS = {
    addTweet(content: string): Effect {
        return {
            io: async () => {
                const post = await http.addPost(content);
                store.update(s => ({ ...s, posts: s.posts.concat(post) }));
            }
        };
    },
    removeTweet(post: Post): Effect {
        return {
            io: async () => {
                await http.deletePost(post);
                updatePost(post.id, (posts, i) => posts.splice(i, 1));
            }
        }
    },
    postTweet(post: Post): Effect {
        if (post.time + post.delay > Date.now()) {
            alert('problem: user can post tweet before delay');
            return;
        }
        return {
            io: async () => {
                await http.post(post);
                updatePost(post.id, (posts, i) => posts[i].resolved = true);
            }
        };
    },
    requestReview(post: Post): Effect {
        if (post.reviewStatus === 'PENDING') {
            return {};
        }
        return {
            io: async () => {
                await http.requestReview(post);
                updatePost(post.id, (posts, i) => posts[i].reviewStatus = 'PENDING');
            }
        }
    },
    getPosts(): Effect {
        return {
            io: async () => {
                const posts = await http.getAllPosts();
                store.update(s => ({ ...s, posts: posts }));
            }
        }
    }
};

(window as any).timeline = [];
store.subscribe(val => (window as any).timeline.push(val));

export function dispatch(actionName: keyof typeof ACTIONS, ...args: any[]) {
    console.info(actionName, args, 'build 1');
    const { io, transform } = ACTIONS[actionName].call(null, ...args) as Effect;

    if (transform != undefined) store.update(transform);
    if (io != undefined) io().catch(error.set);
}