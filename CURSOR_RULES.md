# Cursor Rules for Pydantic-AI Django Project

## Project Structure Management

### 1. File Organization

- Maintain the monorepo structure using Turborepo
- Keep packages isolated and independently versioned
- Follow the established directory structure:
  ```
  pydantic-ai-django/
  ├── apps/
  ├── packages/
  ├── infrastructure/
  └── task-log/
  ```

### 2. Required Documentation Files

- `README.md`: Project overview and setup instructions
- `tree.md`: Current project structure
- `task-log/`: Directory for task documentation
- `infrastructure/README.md`: Infrastructure setup guide

## Task Management

### 1. Task Log Format

Each task must be documented in the `task-log` directory with the format:

```markdown
# Task Name: [XX-task-name]

- **Status**: [In Progress/Complete]
- **Description**: Brief task description
- **Files Changed**:
  - List of modified files
- **Infrastructure Impact**:
  - Any changes to Docker services
  - Database schema updates
- **Project Tree Before/After**:
  - Directory structure changes
- **Timestamp**:
  - Started: YYYY-MM-DD HH:mm:ss
  - Completed: YYYY-MM-DD HH:mm:ss
- **Completion Checklist**:
  - [ ] All subtasks completed
  - [ ] Tests passing
  - [ ] Documentation updated
  - [ ] Code reviewed
```

### 2. Task Naming Convention

- Format for in-progress tasks: `XX-task-[component]-[action].md`
- Format for completed tasks: `XX-task-[component]-[action]-complete.md`
- Examples:
  - In Progress:
    - `01-task-infrastructure-setup.md`
    - `02-task-chat-widget-init.md`
  - Completed:
    - `01-task-infrastructure-setup-complete.md`
    - `02-task-chat-widget-init-complete.md`

### 3. Task Completion Process

1. Rename task file to include `-complete` suffix
2. Update task status to "Complete"
3. Fill completion timestamp
4. Complete the checklist
5. Document any pending items or follow-up tasks
6. Update related documentation

## Development Guidelines

### 1. Infrastructure

- Prefix all Docker services with `pydantic-ai-`
- Maintain separate volumes for each service
- Document all environment variables in `.env.example`
- Use health checks for all services

### 2. Backend (Django)

- Follow Django's app-based structure
- Use UUID for primary keys
- Implement vector search using pgvector
- Document API endpoints in OpenAPI format

### 3. Frontend (Chat Widget)

- Maintain package independence
- Use TypeScript for all components
- Follow component structure:
  ```
  chat-widget/
  ├── src/
  │   ├── components/
  │   ├── hooks/
  │   ├── contexts/
  │   └── utils/
  ```

### 4. Database

- Use migrations for schema changes
- Document vector indexes
- Maintain referential integrity
- Use appropriate field types

## Task Execution Workflow

### Before Starting

1. Check existing documentation:

   - Read `README.md`
   - Review `tree.md`
   - Check related task logs

2. Create task log file:
   ```bash
   touch task-log/XX-task-[name].md
   ```

### During Development

1. Follow component-specific guidelines
2. Document all configuration changes
3. Update environment examples
4. Test service integrations

### After Completion

1. Update project structure:
   ```bash
   ls -R > tree.md
   ```
2. Update relevant README files
3. Complete task log with all changes
4. Verify service health checks

## Safety Checks

### 1. Infrastructure

- Verify Docker service naming
- Check volume persistence
- Validate environment variables
- Test service connectivity

### 2. Code Quality

- Use TypeScript strictly
- Follow ESLint rules
- Maintain code documentation
- Test cross-service communication

### 3. Security

- No hardcoded credentials
- Proper environment variable usage
- Secure file storage configuration
- API authentication implementation

## Version Control

### 1. Commit Messages

Format:

```
[component]: Action description

- Detailed change 1
- Detailed change 2
```

### 2. Branch Naming

Format: `feature/[component]-[description]`
Example: `feature/chat-widget-file-upload`

## Documentation Requirements

### 1. Code Documentation

- TypeScript interfaces
- Component props
- Hook usage examples
- Utility function descriptions

### 2. Infrastructure Documentation

- Service dependencies
- Volume management
- Network configuration
- Backup procedures

### 3. API Documentation

- Endpoint descriptions
- Request/response formats
- Authentication requirements
- Error handling
