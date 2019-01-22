<template>
    <v-container>
        <v-layout justify-center>
            <v-flex align-self-top xs12 md8 lg8 xl6 class="home-container">
                <h1 class="pb-2">About</h1>
                <p class="about-content">&nbsp;&nbsp;&nbsp;&nbsp;The <i>Abstract</i> of the paper - <i>Single Image Haze Removal Using Dark Channel Prior</i> : we propose a simple but effective image prior-dark channel prior to remove haze from a single input image. The dark channel prior is a kind of statistics of the haze-free outdoor images. It is based on a key observation - most local patches in haze-free outdoor images contain some pixels which have very low intensities in at least one color channel. Using this prior with the haze imaging model,we can directly estimate the thickness of the haze and recover a high quality haze-free image. Resultson a variety of outdoor haze images demonstrate the power of the proposed prior. Moreover,a high quality depth map can also be obtained as a by-product of haze removal.</p>
                <p>&nbsp;&nbsp;&nbsp;&nbsp;Our approach is physically valid and are able to handle distant object seven in the heavy haze image. Wedonotrely on signiﬁcant variance on transmission or surface shading in the input image. The result contains few halo artifacts.</p>
                <p>&nbsp;&nbsp;&nbsp;&nbsp;Like any approach using a strong assumption, our approach also has its own limitation. The dark channel prior may be invalid when the scene object is inherently similar totheairlightoveralargelocalregionandnoshadowiscast on the object. Although our approach works well for most of haze outdoor images, it may fail on some extreme cases. We believe that developing novel priors from different directions is very important and combining them together will further advance the state of the art.</p>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<style scoped>
p{
    line-height: 175%;
    font-size: 1.5rem;
}
/* i{
    font-family: "Baskerville";
} */
</style>
