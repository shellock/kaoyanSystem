var valueslist=['哲学', '理论经济学', '应用经济学', '金融学', '统计学', '法学', '政治学', '社会学', '民族学', '马克思主义理论', '公安学', '法律','教育学', '心理学', '体育学', '应用心理学','中国语言文学', '外国语言文学', '新闻传播学','考古学', '中国史', '世界史','数学', '物理学', '化学', '天文学', '地理学', '大气科学', '海洋科学', '地球物理学', '地质学', '生物学', '系统科学', '科学技术史', '生态学', '力学', '材料科学与工程', '电子科学与技术', '计算机科学与技术', '环境科学与工程', '生物医学工程', '基础医学', '公共卫生与预防医学', '药学', '中药学', '医学技术', '护理学',  '机械工程', '光学工程', '仪器科学与技术','冶金工程', '动力工程及工程热物理', '电气工程', '信息与通信工程', '控制科学与工程', '建筑学', '土木工程', '水利工程', '测绘科学与技术', '化学工程与技术', '地质资源与地质工程', '矿业工程', '石油与天然气工程', '纺织科学与工程', '轻工技术与工程', '交通运输工程', '船舶与海洋工程', '航空宇航科学与技术', '兵器科学与技术', '核科学与技术', '农业工程', '林业工程',  '食品科学与工程', '城乡规划学', '风景园林学', '软件工程', '生物工程', '安全科学与工程',  '网络空间安全', '城市规划与设计', '资源与环境',  '交通运输',  '管理科学与工程', '设计学', '作物学', '园艺学', '农业资源与环境', '植物保护', '畜牧学', '兽医学', '林学', '水产', '草学', '农业', '兽医', '风景园林',    '临床医学', '口腔医学',  '中医学', '中西医结合',   '特种医学',   '中医', '工商管理', '农林经济管理', '公共管理', '图书情报与档案管理', '会计学', '旅游管理',  '音乐与舞蹈学', '戏剧与影视学', '美术学'];
var textlist=['(0101)哲学', '(0201)理论经济学', '(0202)应用经济学', '(0251)金融学', '(0270)统计学', '(0301)法学', '(0302)政治学', '(0303)社会学', '(0304)民族学', '(0305)马克思主义理论', '(0306)公安学', '(0351)法律','(0401)教育学', '(0402)心理学', '(0403)体育学', '(0454)应用心理学','(0501)中国语言文学', '(0502)外国语言文学', '(0503)新闻传播学','(0601)考古学', '(0602)中国史', '(0603)世界史','(0701)数学', '(0702)物理学', '(0703)化学', '(0704)天文学', '(0705)地理学', '(0706)大气科学', '(0707)海洋科学', '(0708)地球物理学', '(0709)地质学', '(0710)生物学', '(0711)系统科学', '(0712)科学技术史', '(0713)生态学', '(0772)力学', '(0773)材料科学与工程', '(0774)电子科学与技术', '(0775)计算机科学与技术', '(0776)环境科学与工程', '(0777)生物医学工程', '(0778)基础医学', '(0779)公共卫生与预防医学', '(0780)药学', '(0781)中药学', '(0782)医学技术', '(0783)护理学',  '(0802)机械工程', '(0803)光学工程', '(0804)仪器科学与技术','(0806)冶金工程', '(0807)动力工程及工程热物理', '(0808)电气工程', '(0810)信息与通信工程', '(0811)控制科学与工程', '(0813)建筑学', '(0814)土木工程', '(0815)水利工程', '(0816)测绘科学与技术', '(0817)化学工程与技术', '(0818)地质资源与地质工程', '(0819)矿业工程', '(0820)石油与天然气工程', '(0821)纺织科学与工程', '(0822)轻工技术与工程', '(0823)交通运输工程', '(0824)船舶与海洋工程', '(0825)航空宇航科学与技术', '(0826)兵器科学与技术', '(0827)核科学与技术', '(0828)农业工程', '(0829)林业工程',  '(0832)食品科学与工程', '(0833)城乡规划学', '(0834)风景园林学', '(0835)软件工程', '(0836)生物工程', '(0837)安全科学与工程',  '(0839)网络空间安全', '(0853)城市规划与设计', '(0857)资源与环境',  '(0861)交通运输',  '(0871)管理科学与工程', '(0872)设计学', '(0901)作物学', '(0902)园艺学', '(0903)农业资源与环境', '(0904)植物保护', '(0905)畜牧学', '(0906)兽医学', '(0907)林学', '(0908)水产', '(0909)草学', '(0951)农业', '(0952)兽医', '(0953)风景园林',    '(1002)临床医学', '(1003)口腔医学',  '(1005)中医学', '(1006)中西医结合',   '(1009)特种医学',   '(1057)中医', '(1202)工商管理', '(1203)农林经济管理', '(1204)公共管理', '(1205)图书情报与档案管理', '(1253)会计学', '(1254)旅游管理',  '(1302)音乐与舞蹈学', '(1303)戏剧与影视学', '(1304)美术学'];


window.onload=function(){
	if(!document.getElementById) return;
	if(!document.getElementById('mllb')){
		alert('No such Element');
		return ;
	}
	var selectdom=document.getElementById('mllb');
	for(var i=0;i<valueslist.length;i++){
		var optiondom=document.createElement('option');
		var textnode=document.createTextNode(textlist[i]);
		optiondom.value=valueslist[i];
		optiondom.appendChild(textnode);
		selectdom.appendChild(optiondom);
	}
}