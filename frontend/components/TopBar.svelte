<script>
import TopAppBar, {Row, Section, Title} from '@smui/top-app-bar';
import IconButton from '@smui/icon-button';
import { productName } from '../js/strings';
</script>

<TopAppBar variant="static" color="primary">
    <Row>
        <Section>
            <Title>{productName}</Title>
        </Section>
        {#if false}
        <Section align="end" toolbar>
            <IconButton class="material-icons" aria-label="Home">home</IconButton>
        </Section>
        {/if}
    </Row>
</TopAppBar>