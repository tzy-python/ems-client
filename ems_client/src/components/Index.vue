<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br />

                        <router-link to="/login">安全退出</router-link>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    Welcome! {{user_msg}}
                </h1>
                <table class="table">
                    <tr class="table_header">
                        <td>ID</td>
                        <td>Name</td>
                        <td>Photo</td>
                        <td>Salary</td>
                        <td>Age</td>
                        <td>Age_range</td>
                        <td>Operation</td>
                    </tr>
                    <tr class="row1" v-for="(emp,index) in emp_list" :key="emp.id"
                        :class="index%2==0?'row1': 'row2'">
                        <td>{{emp.id}}</td>
                        <td>{{emp.emp_name}}</td>
                        <td><img :src="emp.img" style="height: 60px;"></td>
                        <td>{{emp.salary}}</td>
                        <td>{{emp.age}}</td>
                        <td>{{emp.age_range}}</td>
                        <td>&nbsp;
                            <router-link :to="'/update/'+emp.id">修改员工</router-link>
                            <a href="javascript:;" @click="delEmp(emp.id)">删除员工</a></td>
                    </tr>
                </table>
                <p>
                    <el-button type="success"><router-link to="/add">添加员工</router-link></el-button>
                </p>
            </div>
        </div>
        <div id="footer">
            <div id="footer_bg">
                ABC@126.com
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Index",
        data(){
          return{
              user_msg:"",
              emp_list:[],
          }
        },
        methods:{
            findAllEmp(){
                this.$axios({
                    url:"http://127.0.0.1:8000/api/emp/",
                    method:"get",
                }).then(res=>{
                    console.log(res.data.results)
                    this.emp_list = res.data.results
                }).catch(error=>{
                    this.$message.error("查询出错了")
                })
            },
            delEmp(id){
                this.emp_list.pop(id=id)
                this.$axios({
                    url:"http://127.0.0.1:8000/api/emp/"+id,
                    method: "delete",
                    data:this.emp_list
                }).then(res=>{
                    this.$message("删除成功")
                    this.$router.push("/index")
                }).catch(res=>{
                    this.$message.error("删除失败")
                })
            }
        },
        created() {
            let username = sessionStorage.getItem("user")
            this.user_msg = username
            if (username){

            } else {
                this.$message.error("请先登录后再访问")
                this.$router.push("/login")
            }
            this.findAllEmp()
        }
    }
</script>

<style scoped>

</style>
