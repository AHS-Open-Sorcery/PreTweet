<div class="container">
  <Tweet canPost postTime={new Date()}>This content is to be reviewed.</Tweet>
</div>

<script>
  import Button, {Label, Icon} from '@smui/button';
  import Tweet from './components/Tweet.svelte';

  let clicked = 0;
</script>

<style>
</style>