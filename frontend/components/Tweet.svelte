<script>
import Card, { Content, Actions, ActionButtons } from '@smui/card';
import Button, { Label, Icon } from '@smui/button';

export let canPost;
export let postTime;
</script>

<Card>
    <div>
        <h2 class="mdc-typography--subtitle2">{postTime.toString()}</h2>
    </div>
    <Content>
        <slot></slot>
    </Content>
    <Actions>
        <ActionButtons>
            <Button disabled={canPost ? null : true} on:click={() => alert("hello!")}>
                <Icon class="material-icons">send</Icon>
                <Label>Post</Label>
            </Button>
            <Button color="secondary">
                <Icon class="material-icons">delete</Icon>
                <Label>Delete</Label>
            </Button>
        </ActionButtons>
    </Actions>
</Card>