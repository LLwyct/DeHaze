<template>
    <v-toolbar flat app prominent color="grey lighten-3" height="75px">
        <v-toolbar-side-icon @click.stop="fuck"></v-toolbar-side-icon>
        <v-toolbar-title to="/fix" tag="v-toolbar-title" class="text-uppercase title display">
            <strong style="font-size: 25px;" @click="toFix">DeHaze</strong>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-sm-and-down">
            <v-btn flat class="toolbar-btn" to="/" replace>home</v-btn>
            <v-btn flat class="toolbar-btn" to="/about" replace>about</v-btn>
            <v-btn flat class="toolbar-btn" to="/fix" replace>fix</v-btn>
        </v-toolbar-items> 
    </v-toolbar>
</template>

<script>
export default {
    data () {
        return {

        }
    },
    methods: {
        toFix () {
            this.$router.replace({
                name: 'fix'
            })
        },
        fuck () {
            this.$store.dispatch('changeDrawerState')
        }
    }
}
</script>


<style scoped>
.toolbar-btn{
    font-size: 18px;
}
.title{
    height: 60%;
    width: 130px;
    display: flex;
    align-items: center;
    transition: 0.3s;
    cursor: pointer;
}
.title:hover{
    transform: scale(1.3);
    text-shadow: 10px 5px 3px #999;
    
}
</style>
