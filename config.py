# This file should be included in .gitignore to not store sensitive data in version control
import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

database_setup = {
   "database_name_production" : "activelix",
   "user_name" : "postgres", # default postgres user name
   "password" : "6210665", # if applicable. If no password, just type in None
   "port" : "localhost:5432" # default postgres port
}
auth0_config = {
    "AUTH0_DOMAIN" : "coffepro.us.auth0.com",
    "ALGORITHMS" : ["RS256"],
    "API_AUDIENCE" : "capstoneapi"
}



bearer_tokens = {
    "customer_service" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVpdnp2SHVySVpuS1dGVnltZTdSUiJ9.eyJpc3MiOiJodHRwczovL2NvZmZlcHJvLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjM4NDhjZmExYjQxZjAwNjc4MTg4MzciLCJhdWQiOiJjYXBzdG9uZWFwaSIsImlhdCI6MTU5NzUyNzEyMCwiZXhwIjoxNTk3NTM0MzIwLCJhenAiOiJkenY1a0VLN0N0YUo3TEw3TjVpd1NWVUYyaTBkdGFlZCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0Om1lbWJlcnMiLCJnZXQ6cGFja2FnZXMiXX0.doxc85CnZyCmVX5GTTXwNZ6HKQQq5ALnrqRI6VYIf9OeBq3Fbt-BfpwHoQnoCqC0qxIqDU1ysDNX7OfvEYp-p2ONrnUh37-xTWVlNL1FmUj_ylXIZR-CFmlVDR7mirGhQrEdvJ40NCvdq_0hxGGydq4i45OdVboS7wE3b28HLRxLP-AJ9uqZ3CFEWPIvO0V2-JAMvfBdnvUFNeudSo90xIWIfhOcXtzk3eFLxBcST_qvi0fVDildP6hwnlBg_c5fM6t4FtzAOwjKBwzT0lDvIFfMvFJykqAnrZJKOrrKYCfHHBpGATNERBt_Gandl-ubi6PsmBRkn2VSNiu0jS4UEQ",
    "supervisor" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVpdnp2SHVySVpuS1dGVnltZTdSUiJ9.eyJpc3MiOiJodHRwczovL2NvZmZlcHJvLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjM4NDhhYTQ3NjY4MzAwNjdlYTg3ODAiLCJhdWQiOiJjYXBzdG9uZWFwaSIsImlhdCI6MTU5NzUyNDY5OCwiZXhwIjoxNTk3NTMxODk4LCJhenAiOiJkenY1a0VLN0N0YUo3TEw3TjVpd1NWVUYyaTBkdGFlZCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOm1lbWJlcnMiLCJnZXQ6bWVtYmVycyIsImdldDpwYWNrYWdlcyIsInBhdGNoOm1lbWJlcnMiLCJwYXRjaDpwYWNrYWdlcyIsInBvc3Q6bWVtYmVycyJdfQ.X7eu0OM7nniMpdiICsHA3JfULMMTp0W-JBDf2e28uZvPzz6EnkpgwA93undTnIlOSE4XDrTx11ppGCXeLqAIqoFtb-vfqMUW636AW_csKso4sMtVUDmtrL0KDFAAyrrsB8uMGTKHrsaZuZshSzQhEXBLNedrsSYWH4wz8A0IecCtOdVFL-AC4-RhHZIM5NP-OgizwNVI1oREfyD2qoSDrGKc3gl6usu75FoZwullFozo3KIrLMGhfG79cDx_Yfwbs-irP6XTYISczcj8kXxbIGPYPCD8ts8ZpwpPvCu8jfgs2dbuUNK4d2VWKT0gFx_ZheZdm3wNsi1c0HbpztIrvA",
    "manger" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVpdnp2SHVySVpuS1dGVnltZTdSUiJ9.eyJpc3MiOiJodHRwczovL2NvZmZlcHJvLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjM4NDg1OWZlNDUyNzAwNmQ5MzI0NDIiLCJhdWQiOiJjYXBzdG9uZWFwaSIsImlhdCI6MTU5NzUyNDM1NiwiZXhwIjoxNTk3NTMxNTU2LCJhenAiOiJkenY1a0VLN0N0YUo3TEw3TjVpd1NWVUYyaTBkdGFlZCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOm1lbWJlcnMiLCJkZWxldGU6cGFja2FnZXMiLCJnZXQ6bWVtYmVycyIsImdldDpwYWNrYWdlcyIsInBhdGNoOm1lbWJlcnMiLCJwYXRjaDpwYWNrYWdlcyIsInBvc3Q6bWVtYmVycyIsInBvc3Q6cGFja2FnZXMiXX0.CIpC-LaQGPvY8x--DpWmWl3JWjnwIbE7QGYzcdGuKnLgH6V2FfURyo69e1IhQ5hz9RJ8ucxeSgobRKrvF2Wd-Z-l801oMU_HRvnec1Mm8Qpyd0FNdPz5qUZKrm7Wloe9vrcYJdhWn0kI9mSfyugNPz0eqUJe8wI229RALeo1eSmjochtqjOzxtbf9bjK3r3JcX4-fzajM8Gg6mFAauJFowojO5IpEnaKfbMNVU4bdb_8SgRMtR3MEdKs62N-9gxZJcbXJy-mC1VIl82ftsR42Z2Tot-oAVqvNQvIBW9fFB5hwfPIT2SOCR9i0K_1g0u6cHfTKiIcg6G7Qfa1kL9s8g"
}
