items = {
	"123": {
		"0001": "test1",
		"0002": "test2",
	},
	"1322": {
		"0003": "test3",
		"0004": "test4",
	},
	"4234": {
		"0005": "test5",
		"0006": "test6",
	}
}

var app = new Vue({
	el: '#app',
	data: {
		items: items
	}
})