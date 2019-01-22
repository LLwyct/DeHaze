<template>
    <v-footer height="auto" color="grey lighten-3" app class="footer">
        <v-layout justify-center row wrap>
            <v-btn v-for="link in links" :key="link.name" color="dark" flat round :href="link.href" target="_blank">{{ link.name }}</v-btn>
            <v-flex grey lighten-3 text-xs-center xs12 class="py-2">&copy;2019 —
                <strong>liwenchi</strong>
            </v-flex>
        </v-layout>
    </v-footer>
</template>

<script>
    export default {
        data: () => ({
            links: [
                {
                    name: 'backend',
                    href: 'https://www.djangoproject.com/'     
                },
                {
                    name: 'Blog',
                    href: 'http://www.cnblogs.com/liwenchi/'     
                },
                {
                    name: 'Contact Us',
                    href: 'https://weibo.com/u/2238952445?refer_flag=1001030103_'     
                }
            ]
        })
    }
</script>
