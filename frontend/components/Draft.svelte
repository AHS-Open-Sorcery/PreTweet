<script>
    import Textfield, {Textarea} from '@smui/textfield';
    import CharacterCounter from '@smui/textfield/character-counter/index';
    import HelperText from '@smui/textfield/helper-text/index';

    export let draftText = '';
</script>

<Textfield fullwidth textarea bind:value={draftText} label="Post Contents"
    input$aria-controls="helper-text" input$aria-described-by="helper-text"
    input$maxlength="280" style="margin: 10px 0; height: 16rem;">
    <CharacterCounter>0 / 280</CharacterCounter>
</Textfield>
