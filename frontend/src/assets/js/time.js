// Date 객체의 연월일이 일치하는지 검사한다.
const isSameDate = function(time1, time2) {
	if (!(time1 instanceof Date) || !(time2 instanceof Date)) {
		console.log("isSameDate: 매개변수가 Date 객체가 아닙니다.")
		return null
	}

	return (time1.getFullYear() === time2.getFullYear()) && _
				 (time1.getMonth() === time2.getMonth()) && _
				 (time1.getDate() === time2.getDate())
}

// 일, 주, 월, 연도의 차이를 계산한다.
const DateDiff = {

	inDays: function(d1, d2) {
		const t2 = d2.getTime();
		const t1 = d1.getTime();

		return parseInt((t2-t1)/(24*3600*1000));
	},

	inWeeks: function(d1, d2) {
		const t2 = d2.getTime();
		const t1 = d1.getTime();

		return parseInt((t2-t1)/(24*3600*1000*7));
	},

	inMonths: function(d1, d2) {
		const d1Y = d1.getFullYear();
		const d2Y = d2.getFullYear();
		const d1M = d1.getMonth();
		const d2M = d2.getMonth();

		return (d2M+12*d2Y)-(d1M+12*d1Y);
	},

	inYears: function(d1, d2) {
		return d2.getFullYear()-d1.getFullYear();
	}
}
export {isSameDate, DateDiff}