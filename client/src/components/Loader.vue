<template>
    <div class="loader">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
    </div>
</template>

<style scoped>
/* body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background: linear-gradient(midnightblue, black);
} */

.loader {
    margin: 0.5em 0;
    width: calc(1em * 7 + 0.15em * 6);
    height: 1.5em;
    display: flex;
    justify-content: space-between;
}

.loader span {
    width: 1em;
    height: 1.5em;
    background-color: skyblue;
    border-radius: 0.15em;
    transform: skewX(-25deg) scale(0.25);
    opacity: 0.25;
    animation: wave 0.75s infinite alternate;
    /* animation-delay: 1s; */
}

.loader span:nth-child(2) {
    animation-delay: 0.15s;
}

.loader span:nth-child(3) {
    animation-delay: 0.3s;
}

.loader span:nth-child(4) {
    animation-delay: 0.45s;
}

.loader span:nth-child(5) {
    animation-delay: 0.6s;
}

.loader span:nth-child(6) {
    animation-delay: 0.75s;
}

@keyframes wave {
    to {
        transform: skew(-25deg) scale(1.0);
        opacity: 1;
    }
}
</style>
