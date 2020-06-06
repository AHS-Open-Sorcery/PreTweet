<script>
    import Dialog, {Title, Content, Actions} from '@smui/dialog';
    import Button, {Label} from '@smui/button';

    export let action; // like 'delete this post', 'request professional review for this post'
    export let onConfirm;

    let dialog;

    export function open() {
        dialog.open();
    }
</script>

<Dialog bind:this={dialog} aria-labelledby="simple-title" aria-describedby="simple-content">
    <Title id="simple-title">
        Are you sure?
    </Title>
    <Content id="simple-content">
        Are you sure you want to {action}?
    </Content>
    <Actions>
        <Button color="secondary">
            No, Cancel
        </Button>
        <Button color="primary" on:click={onConfirm}>
            Yes, Do it
        </Button>
    </Actions>
</Dialog>