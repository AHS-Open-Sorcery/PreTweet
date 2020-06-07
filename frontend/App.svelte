<TopBar />
<ErrorDialog />
<div class="container">
  <PendingTweets />
</div>
<DraftDialog bind:this={draftDialog}></DraftDialog>
<Fab color="secondary" id="draft-fab" on:click={draftDialog.open}>
    <Icon class="material-icons">add</Icon>
</Fab>

<script>
  import { dispatch } from "./js/actions";
  import Button, {Label, Icon} from '@smui/button';
  import Tweet from './components/Tweet.svelte';
  import DraftDialog from './components/DraftDialog.svelte';
  import Fab from '@smui/fab';
  import TopBar from './components/TopBar.svelte';
  import PendingTweets from './components/PendingTweets.svelte';
  import ErrorDialog from './components/ErrorDialog.svelte';

  let draftDialog;

  import { onMount } from 'svelte';

  onMount(async () => {
    dispatch('getPosts');
  })
</script>