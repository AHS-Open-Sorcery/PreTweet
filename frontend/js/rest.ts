import { Post } from "./store";

const defaultInitOptions: RequestInit = {
    credentials: 'include'
};

async function jsonCheckError(response: Response): Promise<any> {
    const json = await response.json();
    if (!response.ok) {
        throw Error(json.error);
    }
    return json;
}

async function GET(endpoint: string): Promise<any> {
    return fetch(endpoint, defaultInitOptions)
        .then(jsonCheckError);
}

async function call(method: string, endpoint: string, data: any): Promise<any> {
    return fetch(endpoint, {
        ...defaultInitOptions,
        method,
        body: JSON.stringify(data)
    })
        .then(jsonCheckError);
}

export async function getAllPosts(): Promise<Post[]> {
    return await GET('/posts');
}

export async function addPost(content: string): Promise<Post> {
    const response = await call('PUT', '/posts', {content, time: Date.now()});
    return response as Post;
}

export async function requestReview(post: Post): Promise<void> {
    await call('POST', '/request-review', post.id);
}

export async function post(post: Post): Promise<void> {
    await call('POST', '/tweet', post.id);
}

export async function deletePost(post: Post): Promise<void> {
    await call('DELETE', '/posts', post.id);
}