<div class="pending-controls">
    <FormField>
        <Checkbox bind:checked={showResolved} />
        <span slot="label">Show posted tweets</span>
    </FormField>
</div>
<div class="pending-tweets">
    {#each shownTweets as tweet}
        <Tweet post={tweet} />
    {:else}
        <i>No tweets yet. Make one!</i>
    {/each}
</div>

<script>
    import FormField from '@smui/form-field';
    import Checkbox from '@smui/checkbox';
    import store from '../js/store';
    import Tweet from './Tweet.svelte';

    let showResolved = false;
    let tweets = [];
    $: shownTweets = showResolved ? tweets : tweets.filter(it => !it.resolved);

    const unsub = store.subscribe(value => tweets = value.posts);
</script>