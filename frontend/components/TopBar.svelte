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
        <Section align="end" toolbar>
            <IconButton class="material-icons" aria-label="Log out"
                onclick="document.location.href = '/logout';">exit_to_app</IconButton>
        </Section>
    </Row>
</TopAppBar>