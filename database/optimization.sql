-- =====================================================
-- ENTERPRISE AI PLATFORM
-- DATABASE OPTIMIZATION SCRIPT
-- =====================================================


-- =====================================================
-- 1. INDEX OPTIMIZATION
-- =====================================================


-- Users

CREATE INDEX IF NOT EXISTS idx_users_email
ON users(email);


CREATE INDEX IF NOT EXISTS idx_users_tenant_id
ON users(tenant_id);



-- Authentication Sessions

CREATE INDEX IF NOT EXISTS idx_sessions_user
ON sessions(user_id);


CREATE INDEX IF NOT EXISTS idx_sessions_token
ON sessions(token);



-- Chat History

CREATE INDEX IF NOT EXISTS idx_chat_user_id
ON chat_history(user_id);


CREATE INDEX IF NOT EXISTS idx_chat_tenant_id
ON chat_history(tenant_id);


CREATE INDEX IF NOT EXISTS idx_chat_created_at
ON chat_history(created_at);



-- Documents

CREATE INDEX IF NOT EXISTS idx_documents_tenant_id
ON documents(tenant_id);


CREATE INDEX IF NOT EXISTS idx_documents_title
ON documents(title);



-- Embeddings / RAG

CREATE INDEX IF NOT EXISTS idx_embeddings_document_id
ON embeddings(document_id);


CREATE INDEX IF NOT EXISTS idx_embeddings_tenant_id
ON embeddings(tenant_id);



-- Workflows

CREATE INDEX IF NOT EXISTS idx_workflows_user_id
ON workflows(user_id);


CREATE INDEX IF NOT EXISTS idx_workflows_status
ON workflows(status);



-- Agents

CREATE INDEX IF NOT EXISTS idx_agents_tenant_id
ON agents(tenant_id);



-- Audit Logs

CREATE INDEX IF NOT EXISTS idx_audit_tenant_id
ON audit_logs(tenant_id);


CREATE INDEX IF NOT EXISTS idx_audit_created_at
ON audit_logs(created_at);





-- =====================================================
-- 2. QUERY OPTIMIZATION
-- =====================================================


-- Authentication Query Optimization

-- BEFORE:
-- SELECT *
-- FROM users
-- WHERE email='user@test.com';


-- AFTER:

SELECT
    id,
    email,
    tenant_id,
    role
FROM users
WHERE email='user@test.com';




-- Chat History Optimization


-- BEFORE:
-- SELECT *
-- FROM chat_history
-- WHERE user_id='123';


-- AFTER:

SELECT
    id,
    message,
    response,
    created_at

FROM chat_history

WHERE user_id='123'

ORDER BY created_at DESC

LIMIT 50;




-- Tenant Document Search Optimization


SELECT
    id,
    title,
    content

FROM documents

WHERE tenant_id='tenant_hr'

AND title ILIKE '%policy%'

LIMIT 20;





-- =====================================================
-- 3. PARTITIONING STRATEGY
-- =====================================================


-- Chat history grows very fast.
-- Partition by month.


CREATE TABLE chat_history_partitioned
(
    id BIGSERIAL,

    tenant_id VARCHAR(100),

    user_id VARCHAR(100),

    message TEXT,

    response TEXT,

    created_at TIMESTAMP

)

PARTITION BY RANGE(created_at);




-- Monthly partitions


CREATE TABLE chat_history_2026_july

PARTITION OF chat_history_partitioned

FOR VALUES FROM
('2026-07-01')

TO
('2026-08-01');





CREATE TABLE chat_history_2026_august

PARTITION OF chat_history_partitioned

FOR VALUES FROM
('2026-08-01')

TO
('2026-09-01');






-- =====================================================
-- 4. CONNECTION POOLING CONFIGURATION
-- =====================================================


-- PostgreSQL example

-- Recommended settings:

-- max_connections = 200
-- shared_buffers = 25% RAM
-- work_mem = 16MB
-- maintenance_work_mem = 512MB



ALTER SYSTEM SET max_connections = 200;


ALTER SYSTEM SET shared_buffers = '2GB';


ALTER SYSTEM SET work_mem = '16MB';






-- =====================================================
-- 5. READ REPLICA STRATEGY
-- =====================================================


-- Primary Database:

-- Handles:
-- INSERT
-- UPDATE
-- DELETE



-- Read Replica:

-- Handles:
-- SELECT queries
-- Analytics
-- Reports
-- Dashboard metrics



-- Example application routing:


-- WRITE:

-- postgres://primary-db:5432/ai_platform



-- READ:

-- postgres://read-replica:5432/ai_platform







-- =====================================================
-- 6. BACKUP STRATEGY
-- =====================================================


-- Daily Full Backup


-- Command:

-- pg_dump ai_platform > backup.sql




-- Continuous WAL Backup


-- Enable:

-- archive_mode = on

-- archive_command =
-- 'cp %p /backup/%f'



-- Recovery Target:

-- Restore Point

-- RPO Target:
-- 5 minutes


-- RTO Target:
-- 30 minutes






-- =====================================================
-- 7. DATABASE PERFORMANCE BENCHMARK
-- =====================================================



-- BEFORE OPTIMIZATION


EXPLAIN ANALYZE

SELECT *

FROM users

WHERE email='test@example.com';




EXPLAIN ANALYZE

SELECT *

FROM chat_history

WHERE user_id='user_1'

ORDER BY created_at;




-- AFTER OPTIMIZATION


EXPLAIN ANALYZE

SELECT

id,
email,
tenant_id

FROM users

WHERE email='test@example.com';





EXPLAIN ANALYZE

SELECT

id,
message,
response,
created_at

FROM chat_history

WHERE user_id='user_1'

ORDER BY created_at DESC

LIMIT 50;





-- =====================================================
-- END DATABASE OPTIMIZATION
-- ===================================================== 