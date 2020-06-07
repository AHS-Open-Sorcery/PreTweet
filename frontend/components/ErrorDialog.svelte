<script>
import { error as errorStore } from "../js/store";
import Button, {Label} from '@smui/button';
import Dialog, {Title, Content, Actions} from '@smui/dialog';

let error = {}, dialog;

errorStore.subscribe(newError => {
    error = newError;
    if (dialog != undefined) {
        dialog.open();
    }
});

</script>
<Dialog bind:this={dialog} aria-labelledby="error-title" aria-describedby="error-message">
    <Title id="error-title">Oopsies!</Title>
    <Content id="error-message">
        There was an error: {error === undefined ? 'something went wrong...' : error.message || 'no message available'}
    </Content>
    <Actions>
        <Button color="primary"><Label>Okay</Label></Button>
    </Actions>
</Dialog>

