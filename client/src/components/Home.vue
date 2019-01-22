<template>
    <v-container>
        <v-layout style="" justify-center>
            <v-flex style="text-align:center" xs12 md8 lg8 xl6 class="home-container">
                <h1 class="home-title pt-4 mt-4">This is a haze-free application.</h1>
                <p class="py-4">The dark channel prior is a kind of statistics of the haze-free outdoor images. Using this prior with the haze imaging model, we can directly estimate the thickness of the haze and recover a high quality haze-free image.</p>
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

p{
    line-height: 175%;
    font-size: 1.5rem;
}
</style>

