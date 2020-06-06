import { writable, Writable } from 'svelte/store';

export type ReviewStatus = {
    status: 'NOT_STARTED'
} | {
    status: 'IN_PROGRESS'
} | {
    status: 'COMPLETE',
    comments: string[]
};

export type Tweet = {
    id: number,
    content: string,
    postTime: Date,
    sentiment: number,
    canPost: boolean,
    review: ReviewStatus
};

export type Store = {
    tweets: Tweet[],
    userToken: string,
    config: {}
};

const store: Writable<Store> = writable({
    tweets: [],
    userToken: '',
    config: {}
});

export default store;