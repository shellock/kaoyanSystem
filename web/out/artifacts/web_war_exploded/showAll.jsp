
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@ page import="entity.MyUser" %>
<%@ page import="java.util.ArrayList" %>
<%@ page import="dao.UserDao" %>
<%@ page import="dao.UserDabImplement" %>
<%@ page import="java.lang.ref.ReferenceQueue" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
    <title>所有用户页面</title>
</head>

<body>

<!--以下两段代码放在body中不要放在<html>之外-->
<%
    String path=request.getContextPath();
    String basepath=request.getScheme()+"://"+ request.getServerName()+":"+request.getServerPort()+"/";
%>
<!-- 使用from提交数据，不能在不刷新页面的情况下直接在当前页面显示处理过的后台数据-->
<c:forEach var="U" items="${requestScope.get('all')}"  >
    <form action="updateServlet" method="post">
        <tr>
            <td><input type="text" value="${U.name}" name="name" ></td>
            <td><input type="text" value="${U.password}" name="password"></td>
            <td><input type="text" value="${U.id}" name="id"></td>
            <td><a href="DeleteServlet?id=${U.id}">删除</a> <input type="submit" value="更新"/></td>
        </tr>
    </form>
</c:forEach>
</body>
</html>
