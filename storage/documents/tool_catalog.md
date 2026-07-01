# MCP Tool Catalog

## Server Name
Company Tools Server

---

## Available Tools

### 1. calculator

Performs arithmetic calculations.

#### Parameters

| Parameter | Type | Description |
|------------|--------|-------------|
| operation | string | add, subtract, multiply, divide |
| a | float | First number |
| b | float | Second number |

#### Example

```json
{
  "operation": "add",
  "a": 10,
  "b": 20
}
```

Result:

```json
30
```

---

### 2. leave_balance

Returns employee leave balance.

#### Parameters

| Parameter | Type |
|------------|--------|
| employee_id | string |

Example:

```json
{
  "employee_id": "EMP001"
}
```

Result:

```json
12
```

---

### 3. payroll_lookup

Returns payroll details.

#### Parameters

| Parameter | Type |
|------------|--------|
| employee_id | string |

Example:

```json
{
  "employee_id": "EMP001"
}
```

Result:

```json
{
  "salary": 50000,
  "month": "June"
}
```

---

### 4. project_status_lookup

Returns project status.

#### Parameters

| Parameter | Type |
|------------|--------|
| project_id | string |

Example:

```json
{
  "project_id": "PRJ001"
}
```

Result:

```json
"In Progress"
```

---

### 5. knowledge_search

Searches the company knowledge base.

#### Parameters

| Parameter | Type |
|------------|--------|
| topic | string |

Example:

```json
{
  "topic": "leave policy"
}
```

Result:

```json
"Employees receive 15 annual leave days."
```

---

## MCP Exposure

All tools are exposed using:

```python
@mcp.tool()
```

and are available through the MCP server for client access.