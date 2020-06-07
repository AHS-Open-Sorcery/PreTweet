<script>import { dispatch } from "../js/actions";

import Draft from "./Draft.svelte";
import Dialog, {Title, Content, Actions} from '@smui/dialog';
import Button, {Icon as FIcon} from '@smui/button';

let dialog, text = '';

export function open() {
    dialog.open();
}

function discard() {
    text = "";
}

function submit() {
    dispatch('addTweet', text);
}

</script>

<Dialog bind:this={dialog}>
    <Title class="draft-title">Draft a New Post</Title>
    <Content class="draft-content">
        <Draft bind:draftText={text}></Draft>
    </Content>
    <Actions>
        <Button color="secondary" on:click={discard}><FIcon class="material-icons">delete</FIcon> Discard</Button>
        <Button color="primary" default on:click={submit} disabled={text.trim().length === 0}><FIcon class="material-icons">send</FIcon> Submit</Button>
    </Actions>
</Dialog>