<%--
  Created by IntelliJ IDEA.
  User: Shellock Holmes
  Date: 2020/5/10
  Time: 11:52
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" import="java.util.*" pageEncoding="UTF-8" language="java" %>
<%@ page import="entity.Schools" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
    <title>学校推荐</title>
    <meta http-equiv="Content-Type" content="text/html charset=UTF-8">
    <link rel="stylesheet" media="screen" href='styles/basic.css'/>
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
<div class="container">
    <div class="row">
        <div class="form-box">
            <div class="form-summary">
            我们收集学校历年数据构建评分模型为其打分，本次搜素按得分由高到低列出结果。
            </div>
            <div class="form">

                <form name="form1" id="form1"  >
                    <c:forEach var="school" items="${requestScope.get('schoolList')}">
                        <table id="schoolTable" style="border-color: grey;">
                            <tr>
                                <td>
                                    院校名称：${school.name}
                                </td>
                                <td>
                                    所属地区：${school.area}
                                </td>
                                <td>
                                    分数线：${school.score}
                                </td>
                                <td>
                                    科目1：${school.subject1}
                                </td>
                                <td>
                                    科目2：${school.subject2}
                                </td>
                                <td>
                                    科目3：${school.subject3}
                                </td>
                                <td>
                                    科目4：${school.subject4}
                                </td>
                                <td>
                                    <a href="${school.href}">更多信息</a>
                                </td>
                            </tr>
                        </table>
                    </c:forEach>
                </form>
            </div>
        </div>
    </div>
</div>
</body>
</html>
