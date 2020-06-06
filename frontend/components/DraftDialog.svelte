<script>
import Draft from "./Draft.svelte";
import Dialog, {Title, Content, Actions} from '@smui/dialog';
import Button, {Icon as FIcon} from '@smui/button';

let dialog;

export function open() {
    dialog.open();
}

</script>

<Dialog bind:this={dialog}>
    <Title class="draft-title">Draft a New Post</Title>
    <Content class="draft-content">
        <Draft></Draft>
    </Content>
    <Actions>
        <Button color="secondary"><FIcon class="material-icons">delete</FIcon> Discard</Button>
        <Button color="primary" default><FIcon class="material-icons">send</FIcon> Submit</Button>
    </Actions>
</Dialog>