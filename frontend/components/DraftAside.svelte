<script>import { dispatch } from "../js/actions";

import Draft from "./Draft.svelte";
import Card, {Content, Actions} from '@smui/card';
import Button, {Icon} from '@smui/button';

let text = '';

</script>

<Card padded style="min-width: 400px">
    <div>
        <span class="mdc-typography--headline6">Draft a New Post</span>
    </div>
    <Content>
        <Draft bind:draftText={text} />
    </Content>
    <Actions>
        <Button color="secondary" on:click={() => text = ''}>
            <Icon class="material-icons">delete</Icon>
            Clear
        </Button>
        <Button color="primary" disabled={text.trim().length === 0 ? true : null}
                on:click={() => { dispatch('addTweet', text); text = ''; }}>
            <Icon class="material-icons">send</Icon>
            Submit
        </Button>
    </Actions>
</Card>