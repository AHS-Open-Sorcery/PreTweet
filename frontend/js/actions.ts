import dayjs from 'dayjs';
import store, { Store } from './store';

type Transformer = (store: Store) => Store;

export const ACTIONS = {
    addTweet(content: string): Transformer {
        console.info(`called addTweet with content ${content}`);
        console.log(dayjs());
        return s => s;
    },
    removeTweet(id: string): Transformer {
        console.info(`remove ${id}`);
        return s => s;
    }
};

export function dispatch(actionName: keyof typeof ACTIONS, ...args: any[]) {
    console.info(actionName, args);
    update(ACTIONS[actionName].call(null, args) as Transformer);
}

function update(t: Transformer) {
    store.update(t);
}