import { writable, Writable } from 'svelte/store';

export interface Review {
    id: number;
    reviewerId: number;
    time: number;
    comments: string[];
}

export interface Post {
    id: number,
    content: string,
    time: number,
    sentiment: number,
    delay: number,
    reviewStatus: 'NOT_STARTED' | 'PENDING' | 'COMPLETE',
    reviews: Review[],
    resolved: boolean
};

export type Store = {
    posts: Post[],
    userToken: string,
    config: {}
};

const store: Writable<Store> = writable({
    posts: [],
    userToken: '',
    config: {}
});

export default store;

export const error: Writable<Error|undefined> = writable(undefined);