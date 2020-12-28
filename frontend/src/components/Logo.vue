<template>
	<router-link tag="a" :to="to" class="logo no-drag" :class="{'text-small' : sizable && $vuetify.breakpoint.smAndDown}">
		<span v-if="!plain">&lt;</span> Mini<span class="py">Py</span> <span v-if="!plain">&gt;</span>
	</router-link>
</template>

<script>
export default {
name: 'Logo',
props: {
	to : {
		type: [ Object, String ],
		default: () => ({name: 'Main'})
	},
	plain : {
		type: Boolean,
		default: () => false
	},
	sizable: {
		type: Boolean,
		default: () => false
	}
}
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Recursive:wght@300;400;500&display=swap');
.logo {
	font-family: 'Recursive', sans-serif;
	font-weight: 300;
	font-size: 2em;
	text-decoration: none;
	color: inherit;
}
.logo .py {
	color: rgb(55,115,165);
}
.no-drag {
	-ms-user-select: none; 
	-moz-user-select: -moz-none;
	-webkit-user-select: none; 
	-khtml-user-select: none; 
	user-select:none;
}
.text-small {
	font-size: 1.5em !important;
}
</style>