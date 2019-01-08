<template>
    <v-toolbar flat app prominent color="grey lighten-3" height="75px">
        <v-toolbar-title to="/fix" tag="v-toolbar-title" class="text-uppercase title hidden-xs-and-down">
            <strong style="font-size: 25px;" @click="toFix">&nbsp;&nbsp;&nbsp;DeHaze</strong>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
            <v-btn flat class="toolbar-btn" to="/" replace>home</v-btn>
            <v-btn flat class="toolbar-btn" to="/about" replace>about</v-btn>
            <v-btn flat class="toolbar-btn" to="/fix" replace>fix</v-btn>
            <!-- <v-btn flat class="toolbar-btn" @click="toabout"> about </v-btn>
            <v-btn flat class="toolbar-btn" @click="tofix">fix</v-btn> -->
        </v-toolbar-items> 
    </v-toolbar>
</template>

<script>
export default {
    methods: {
        toFix () {
            this.$router.replace({
                name: 'fix'
            })
        }
    }
}
</script>


<style scoped>
.toolbar-btn{
    font-size: 18px;
}
.title{
    transition: 0.3s;
    cursor: pointer;
}
.title:hover{
    transform: scale(1.1)
}
</style>
