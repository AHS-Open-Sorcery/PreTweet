<script>
import Card, { Content, Actions, ActionButtons, ActionIcons } from '@smui/card';
import Button, { Label, Icon as BtnIcon } from '@smui/button';
import { Icon } from '@smui/common';
import List, {Item, Text, PrimaryText, SecondaryText} from '@smui/list';
import Menu from '@smui/menu';
import IconButton from '@smui/icon-button';
import { Anchor } from '@smui/menu-surface';
import { dispatch } from '../js/actions';
import * as fmt from '../js/format';
import Confirm from './Confirm.svelte';

export let canPost//: boolean;
export let postTime//: Date;
export let positivity = Math.random() * 2 - 1; //: number = 0; // [-1, 1]

$: positivityFormat = {
    color: fmt.colorRating((positivity + 1) / 2),
    message: 'This post is ' + (() => {
        const mag = Math.abs(positivity);
        if (mag < 0.15) {
            return 'roughly neutral';
        }
        return fmt.quantifyAmount(mag) + (positivity > 0 ? ' nice' : ' mean');
    })(),
    icon: fmt.iconRating((positivity + 1) / 2)
};

let moreAnchor, moreMenu;
let deleteConfirm;

</script>

<Card>
    <div style="padding: 1rem 1rem 0 1rem">
        <h3 class="mdc-typography--subtitle2" style="margin: 0; color: #999;">
            Submitted {fmt.formatDateTime(postTime)}
        </h3>
        <h3 class="mdc-typography--subtitle2" style="margin: 0; color: {positivityFormat.color}">
            <Icon class="material-icons" style="font-size: 12px;">{positivityFormat.icon}</Icon>
            {positivityFormat.message}
        </h3>
    </div>
    <Content class="mdc-typography--headline5">
        <slot></slot>
    </Content>
    <Actions>
        <ActionButtons>
            <Button disabled={canPost ? null : true} on:click={() => dispatch('addTweet', 'hello')}>
                <BtnIcon class="material-icons">send</BtnIcon>
                <Label>Post</Label>
            </Button>
            <Button color="secondary" on:click={deleteConfirm.open}>
                <BtnIcon class="material-icons">delete</BtnIcon>
                <Label>Delete</Label>
            </Button>
            <Confirm bind:this={deleteConfirm}
                action="delete this post" onConfirm={() => dispatch('removeTweet', 12345)}></Confirm>
        </ActionButtons>
        <ActionIcons>
            <div use:Anchor bind:this={moreAnchor}>
                <IconButton class="material-icons" title="More options" on:click={() => moreMenu.setOpen(true)}>more_vert</IconButton>
                <Menu bind:this={moreMenu} anchor={false} bind:anchorElement={moreAnchor} anchorCorner="BOTTOM_LEFT">
                    <List>
                        <Item>
                            <Text>Request Review</Text>
                        </Item>
                    </List>
                </Menu>
            </div>
        </ActionIcons>
    </Actions>
</Card>