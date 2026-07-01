--Documents
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    department VARCHAR(100),
    owner VARCHAR(100),
    version INT DEFAULT 1,
    status VARCHAR(50) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--Document_Chunks
CREATE TABLE document_chunks (
    id SERIAL PRIMARY KEY,
    document_id INT NOT NULL,
    chunk_number INT NOT NULL,
    chunk_text TEXT NOT NULL,
    embedding_id VARCHAR(255),
    page_number INT,

    CONSTRAINT fk_document
        FOREIGN KEY(document_id)
        REFERENCES documents(id)
        ON DELETE CASCADE
);

-- Document_Versions
CREATE TABLE document_versions (
    id SERIAL PRIMARY KEY,
    document_id INT NOT NULL,
    version INT NOT NULL,
    uploaded_by VARCHAR(100),
    approved_by VARCHAR(100),
    approval_date TIMESTAMP,

    CONSTRAINT fk_version_document
        FOREIGN KEY(document_id)
        REFERENCES documents(id)
        ON DELETE CASCADE
);

-- Document_Permissions
CREATE TABLE document_permissions (
    id SERIAL PRIMARY KEY,
    role VARCHAR(100),
    department VARCHAR(100),
    access_level VARCHAR(50)
);

-- Indexes
CREATE INDEX idx_documents_department
ON documents(department);

CREATE INDEX idx_documents_status
ON documents(status);

CREATE INDEX idx_chunks_document
ON document_chunks(document_id);

CREATE INDEX idx_versions_document
ON document_versions(document_id);