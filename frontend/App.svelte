<TopBar />
<div class="container">
  <Tweet canPost postTime={new Date()}>This content is to be reviewed.</Tweet>
  
</div>
<DraftDialog bind:this={draftDialog}></DraftDialog>
<Fab color="secondary" id="draft-fab" on:click={draftDialog.open}>
    <Icon class="material-icons">add</Icon>
</Fab>

<script>
  import Button, {Label, Icon} from '@smui/button';
  import Tweet from './components/Tweet.svelte';
  import DraftDialog from './components/DraftDialog.svelte';
  import Fab from '@smui/fab';
  import TopBar from './components/TopBar.svelte';

  let draftDialog;
</script>