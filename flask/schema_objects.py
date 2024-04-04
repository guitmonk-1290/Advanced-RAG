from llama_index.core.objects import (
    SQLTableSchema,
)

table_schema_objs = [
    (SQLTableSchema(
        table_name="admin",
        context_str="This table stores information about all the admins in the database."
    )),
    (SQLTableSchema(table_name="admin_roles")),
    (SQLTableSchema(table_name="amc_overrides")),
    (SQLTableSchema(
        table_name="clients",
        context_str="This table gives information about all the clients regarding their name, type, code, contact, address, status and other related information."
    )),
    (SQLTableSchema(
        table_name="client_groups",
        context_str="This table stores information about client groups."
    )),
    (SQLTableSchema(
        table_name="client_management_amcs"
    )),
    (SQLTableSchema(
        table_name="client_management_companies",
        context_str="This table stores information about the management companies for clients. Use this table only when the query is related to management companies."
    )),
    (SQLTableSchema(
        table_name="client_management_customizes"
    )),
    (SQLTableSchema(
        table_name="client_management_devices"
    )),
    (SQLTableSchema(
        table_name="client_management_hardwares"
    )),
    (SQLTableSchema(
        table_name="client_management_locations"
    )),
    (SQLTableSchema(
        table_name="client_management_softwares"
    )),
    (SQLTableSchema(
        table_name="client_management_syncsummaries"
    )),
    (SQLTableSchema(
        table_name="client_management_systeminfos"
    )),
    (SQLTableSchema(
        table_name="client_mappings"
    )),
    (SQLTableSchema(
        table_name="client_ticket_feedbacks",
        context_str="This tables stores information about the tickets used for feedback by the clients."
    )),
    (SQLTableSchema(table_name="comments")),
    (SQLTableSchema(table_name="config_masters")),
    (SQLTableSchema(table_name="contact_managements")),
    (SQLTableSchema(table_name="departments")),
    (SQLTableSchema(table_name="document_attributes")),
    (SQLTableSchema(table_name="document_downloads")),
    (SQLTableSchema(table_name="document_mail_histories")),
    (SQLTableSchema(table_name="document_solutions")),
    (SQLTableSchema(table_name="document_upload_histories")),
    (SQLTableSchema(table_name="document_uploads")),
    (SQLTableSchema(table_name="email_sends")),
    (SQLTableSchema(table_name="hoilday_masters")),
    (SQLTableSchema(table_name="industries")),
    (SQLTableSchema(table_name="issue_management_histories")),
    (SQLTableSchema(table_name="issue_managements")),
    (SQLTableSchema(table_name="lead_comments")),
    (SQLTableSchema(table_name="lead_managements")),
    (SQLTableSchema(table_name="lead_milestones")),
    (SQLTableSchema(table_name="license_histories")),
    (SQLTableSchema(
        table_name="license_issue_masters",
        context_str="This table stores information about the licenses issued and their status. This table is used if the user wants information about a client's license."
    )),
    (SQLTableSchema(table_name="license_issue_summaries")),
    (SQLTableSchema(table_name="menu_masters")),
    (SQLTableSchema(table_name="partners")),
    (SQLTableSchema(table_name="product_page_masters")),
    (SQLTableSchema(table_name="product_release_directories")),
    (SQLTableSchema(table_name="product_release_downloads")),
    (SQLTableSchema(table_name="product_release_histories")),
    (SQLTableSchema(table_name="product_releases")),
    (SQLTableSchema(table_name="product_variant_masters")),
    (SQLTableSchema(table_name="products")),
    (SQLTableSchema(table_name="role_permissions")),
    (SQLTableSchema(table_name="sla_client")),
    (SQLTableSchema(table_name="sla_grades")),
    (SQLTableSchema(table_name="solutions")),
    (SQLTableSchema(table_name="tag_masters")),
    (SQLTableSchema(table_name="task_managements")),
    (SQLTableSchema(table_name="team_members")),
    (SQLTableSchema(table_name="teams")),
    (SQLTableSchema(table_name="ticket_comments")),
    (SQLTableSchema(table_name="task_managements")),
    (SQLTableSchema(table_name="ticket_solution_histories")),
    (SQLTableSchema(table_name="ticket_solution_like_dislikes")),
    (SQLTableSchema(table_name="ticket_solution_views")),
    (SQLTableSchema(table_name="ticket_solutions")),
    (SQLTableSchema(table_name="ticket_status_activities")),

]  # add a SQLTableSchema for each table
