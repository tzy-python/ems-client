<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br />
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">Main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    add Emp info:
                </h1>
                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">
                            name:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="name" v-model="emp_name"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            photo:
                        </td>
                        <td valign="middle" align="left">
                            <input type="file" name="photo" ref="photo"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            salary:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="salary" v-model="salary"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            age:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="age" v-model="age"/>
                        </td>
                    </tr>
                </table>
                <p>
                    <input type="submit" class="button" value="点击添加" @click="addEmp"/>
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
        name: "Add_emp",
        data(){
            return{
                emp_name:"",
                img:"",
                salary:"",
                age:"",
            }
        },
        methods:{
            addEmp(){
                let photo = this.$refs.photo.files[0]
                let formData = new FormData()
                formData.append("emp_name",this.emp_name)
                formData.append("img",photo)
                formData.append("salary",this.salary)
                formData.append("age",this.age)
                this.$axios({
                    url:"http://127.0.0.1:8000/api/emp/",
                    method:"post",
                    data:formData,
                    headers:{
                        "content-type":"multipart/form-data"
                    }
                }).then(res=>{
                    console.log(res.data)
                    this.$router.push("/index")
                }).catch(error=>{
                    this.$message.error("添加失败")
                })
            }
        }
    }
</script>

<style scoped>

</style>
