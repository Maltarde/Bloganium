const app = ({
    data() {
        return {
            mod: window.matchMedia('(prefers-color-scheme: dark)').matches,
            showMenu: false,
        }
    },
    created() {
        const is_mod = sessionStorage.getItem("mod");
        if(is_mod === "dark") {
            this.mod = true
        } else if(is_mod === "light") {
            this.mod = false
        }
        this.setMod()
    },
    mounted() {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
            sessionStorage.removeItem("mod");
            this.mod = e.matches ? true : false
            this.setMod()
        })
    },
    methods: {
        changeMod() {
            this.mod = !this.mod
            this.setMod()

            if (this.mod == true) {
                sessionStorage.setItem("mod", "dark");
            } else {
                sessionStorage.setItem("mod", "light");
            }
        },
        setMod() {
            if (this.mod == true) {
                document.documentElement.setAttribute("data-theme", "dark");
            } else {
                document.documentElement.setAttribute("data-theme", "light");
            }
        },
        getSession() {
            
            
        }

    }
})
Vue.createApp(app).mount("#app");