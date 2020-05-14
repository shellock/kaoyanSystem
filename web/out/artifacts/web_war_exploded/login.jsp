<%--
  Created by IntelliJ IDEA.
  User: Shellock Holmes
  Date: 2020/5/1
  Time: 12:27
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>考研高校查询_高校推荐系统</title>
    <link rel="stylesheet" media="screen" href='styles/basic.css'/>
    <script src="scripts/jquery-3.4.1.min.js"></script>
    <script src="scripts/mllbInit.js"></script>
    <script src="scripts/zymcChange.js"></script>
</head>
<body>
<div class="header-wrapper">
    <div class="header-second ">
        <h1>考研高校推荐系统</h1>
        <div class="header-quotes">
            致力于解决择校难问题！
        </div>
    </div>
</div>
<!--上边是头部目录-->
<!--接下来直接填写表单-->
<div class="container">
    <div class="row">
        <div class="form-box">
            <h2>填写表单</h2>
            <div class="form-summary">
                专业名称和预期分数为必选项，所在省市可以不填
            </div>
            <div class="form">
                <form name="form1" method="post" id="form1" action="FormSubmitServlet" >
                    <table border="0" cellspacing="0" cellpadding="0">
                        <colgroup>
                            <col width="120">
                            <col width="260">
                        </colgroup>
                        <tbody>
                        <tr>
                            <td align="right">
                                <label>所在省市</label>
                            </td>
                            <td align="left">
                                <select name="szss" id="szss" class="select">
                                    <option value>--选择省市--</option>
                                    <option value="北京市">(11)北京市</option>
                                    <option value="天津市">(12)天津市</option>
                                    <option value="河北省">(13)河北省</option>
                                    <option value="山西省">(14)山西省</option>
                                    <option value="内蒙古自治区">(15)内蒙古自治区</option>
                                    <option value="辽宁省">(21)辽宁省</option>
                                    <option value="吉林省">(22)吉林省</option>
                                    <option value="黑龙江省">(23)黑龙江省</option>
                                    <option value="上海市">(31)上海市</option>
                                    <option value="江苏省">(32)江苏省</option>
                                    <option value="浙江省">(33)浙江省</option>
                                    <option value="安徽省">(34)安徽省</option>
                                    <option value="福建省">(35)福建省</option>
                                    <option value="江西省">(36)江西省</option>
                                    <option value="山东省">(37)山东省</option>
                                    <option value="河南省">(41)河南省</option>
                                    <option value="湖北省">(42)湖北省</option>
                                    <option value="湖南省">(43)湖南省</option>
                                    <option value="广东省">(44)广东省</option>
                                    <option value="广西壮族自治区">(45)广西壮族自治区</option>
                                    <option value="海南省">(46)海南省</option>
                                    <option value="重庆市">(50)重庆市</option>
                                    <option value="四川省">(51)四川省</option>
                                    <option value="贵州省">(52)贵州省</option>
                                    <option value="云南省">(53)云南省</option>
                                    <option value="西藏自治区">(54)西藏自治区</option>
                                    <option value="陕西省">(61)陕西省</option>
                                    <option value="甘肃省">(62)甘肃省</option>
                                    <option value="青海省">(63)青海省</option>
                                    <option value="宁夏回族自治区">(64)宁夏回族自治区</option>
                                    <option value="新疆维吾尔自治区">(65)新疆维吾尔自治区</option>
                                </select>
                            </td>
                        </tr>
                        <tr>
                            <td align="right">
                                <label>专业名称</label>
                            </td>
                            <td align="left">
                                <select name="mllb" id="mllb" class="select mllb" >
                                    <option value>--选择专业--</option>
                                </select>
                            </td>
                        </tr>
                        <tr>
                            <td align="right">
                                <label>预期分数</label>
                            </td>
                            <td align="left">
                                <input name="yqfs" type="text" id="yqfs">
                            </td>
                        </tr>
                        <tr>
                            <td class="text_enter" colspan="4">
                                <input type="submit" name="button" id="button_submint" class="btn"
                                       value="查询">
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </form>
            </div>
            <!-- 表单 end-->
        </div>
        <div class="placeholder">
            <!--这里是查询结果展示区域-->
        </div>
    </div>
</div>
</body>
</html>