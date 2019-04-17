<template>
    <v-container>
            <v-layout>
                <v-flex>
                    <h1 class="home-title">This is a haze removal application</h1>
                </v-flex>
            </v-layout>
            <v-layout justify-center>
                <v-flex md8 my-3>
                    <p>The dark channel prior is a kind of statistics of the haze-free outdoor images. Using this prior
                        with the haze imaging model, we can directly estimate the thickness of the haze and recover a
                        high quality haze-free image.</p>
                </v-flex>
            </v-layout>
            <v-layout justify-center>
                <v-flex md4 my-3>
                    <v-btn block outline to="/fix" replace>DEHAZE IMAGE</v-btn>
                </v-flex>
            </v-layout>
    </v-container>
</template>

<style scoped>
.home-title{
    font-size:  50px;
    text-align: center;
}

p{
    line-height: 175%;
    font-size: 1.5rem;
    text-align: center;
}
</style>

