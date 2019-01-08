<template>
    <v-container>
        <v-layout style="height: 40vh;margin-top: 30px;" justify-center>
            <v-flex align-self-top style="text-align:center" xs12 md8 lg6 class="home-container">
                <h1 class="home-title pt-4 mt-4">This is a dehaze application.</h1>
                <h3 class="py-4">Extend your GitHub workflow beyond your browser with GitHub Desktop, completely redesigned with Electron. Get a unified cross-platform experience that’s completely open source and ready to customize.</h3>
                <v-flex xs12 md8 offset-md2 lg6 offset-lg3 class="py-4 mt-4">
                    <v-btn block outline to="/fix" replace>DEHAZE IMAGE</v-btn>
                </v-flex>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<style scoped>
.home-title{
    font-size:  50px;
}
</style>

