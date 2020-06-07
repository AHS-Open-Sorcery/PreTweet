<script>import store from '../js/store';

import Card, { Content, Actions, ActionButtons, ActionIcons } from '@smui/card';
import Button, { Label, Icon as BtnIcon } from '@smui/button';
import { Icon } from '@smui/common';
import {Row, Section, Title} from '@smui/top-app-bar';
import List, {Item, Text, PrimaryText, SecondaryText, Separator} from '@smui/list';
import Menu from '@smui/menu';
import IconButton from '@smui/icon-button';
import { Anchor } from '@smui/menu-surface';
import { dispatch } from '../js/actions';
import * as fmt from '../js/format';
import Confirm from './Confirm.svelte';

export let post;

$: positivityFormat = {
    color: fmt.colorRating((post.sentiment + 1) / 2),
    message: 'This post is ' + (() => {
        const mag = Math.abs(post.sentiment);
        if (mag < 0.15) {
            return 'roughly neutral';
        }
        return fmt.quantifyAmount(mag) + (post.sentiment > 0 ? ' nice' : ' mean');
    })(),
    icon: fmt.iconRating((post.sentiment + 1) / 2)
};

const reviewStatusFormats = {
    'PENDING': ['hourglass_empty', 'Review Pending', 'rgba(173, 168, 0, 1)'],
    'COMPLETE': ['done', 'Reviewed', 'rgba(0, 133, 11, 1)']
}
$: reviewStatusFormat = reviewStatusFormats[post.reviewStatus];

let canPost = post.time + post.delay * 1000 <= Date.now();
let fontSize = 1.5 - (post.content.length / 280 * 0.5);

let moreAnchor, moreMenu;
let deleteConfirm;

let commentsVisible = false;

</script>

<div class="tweet" resolved={post.resolved ? true : null}>
    <Card style="max-width: 500px">
        {#if post.reviewStatus !== 'NOT_STARTED'}
        <div style="padding: 0.7rem; background-color: {reviewStatusFormat[2]}; display: flex; border-radius: 2px;" class="mdc-typography--body1">
            <Icon class="material-icons" style="font-size: 20px">{reviewStatusFormat[0]}</Icon>
            &nbsp;
            {reviewStatusFormat[1]}
        </div>
        {/if}
        <div style="padding: 1rem 1rem 0 1rem">
            <h3 class="mdc-typography--subtitle2" style="margin: 0; color: #999;">
                Submitted {fmt.formatDateTime(new Date(post.time))}
            </h3>
            <h3 class="mdc-typography--subtitle2" style="margin: 0; color: {positivityFormat.color}">
                <Icon class="material-icons" style="font-size: 12px;">{positivityFormat.icon}</Icon>
                {positivityFormat.message}
            </h3>
        </div>
        <Content style="font-size: {fontSize}em;">
            {post.content}
        </Content>
        <Actions>
            <ActionButtons>
                <Button disabled={canPost && !post.resolved ? null : true} on:click={() => dispatch('postTweet', post)}>
                    {#if !post.resolved}
                        <BtnIcon class="material-icons">send</BtnIcon>
                    {/if}
                    <Label>{post.resolved ? 'Posted' : 'Post'}</Label>
                </Button>
                <Button color="secondary" on:click={deleteConfirm.open}>
                    <BtnIcon class="material-icons">delete</BtnIcon>
                    <Label>Delete</Label>
                </Button>
                <Confirm bind:this={deleteConfirm}
                    action="delete this post" onConfirm={() => dispatch('removeTweet', post)}></Confirm>
            </ActionButtons>
            <ActionIcons>
                <div use:Anchor bind:this={moreAnchor}>
                    <IconButton class="material-icons" title="More options" on:click={() => moreMenu.setOpen(true)}>more_vert</IconButton>
                    <Menu bind:this={moreMenu} anchor={false} bind:anchorElement={moreAnchor} anchorCorner="BOTTOM_LEFT">
                        <List>
                            <Item on:click={() => dispatch('requestReview', post)} disabled={post.reviewStatus === 'PENDING' ? true : null}>
                                <Text>Request Review</Text>
                            </Item>
                        </List>
                    </Menu>
                </div>
            </ActionIcons>
        </Actions>
        {#if post.reviewStatus === 'COMPLETE'}
            <Separator />
            <div style="padding: 10px;">
            <Row>
                <Section>
                    <h4 class="mdc-typography--subtitle2">REVIEWER COMMENTS</h4>
                </Section>
                <Section align="end" toolbar>
                    <IconButton class="material-icons expander" expanded={commentsVisible ? true : null}
                        on:click={() => { commentsVisible = !commentsVisible }}>keyboard_arrow_up</IconButton>
                </Section>
            </Row>
            <List nonInteractive class="tweet-comments" open={commentsVisible ? true : null}>
                {#each post.reviews as review} 
                    {#each review.comments as comment}
                    <Item ripple={false}>
                        <Text>
                            {comment}
                        </Text>
                    </Item>
                    {/each}
                    <Separator />
                {/each}
            </List>
            </div>
        {/if}
    </Card>
</div>

<style>
    div.tweet[resolved] {
        filter: brightness(85%);
    }

    .expander {
        transition: transform 0.2s ease-in-out;
    }
    .expander[expanded] {
        transform: rotate(180deg);
    }
</style>