# Pydantic AI Django Project

A modern AI-powered application built with Django, React, and Pydantic.

## Prerequisites

- Node.js >= 18
- PNPM >= 8.15.4
- Python >= 3.11
- Docker and Docker Compose

## Project Structure

```
├── apps/
│   ├── backend/     # Django backend application
│   │   ├── api/    # REST API app
│   │   ├── chat/   # Chat functionality app
│   │   └── config/ # Django settings
│   └── frontend/   # Next.js frontend application
├── packages/
│   ├── ui/         # Shared UI components
│   ├── types/      # Shared TypeScript types
│   └── chat-widget/# Chat widget package
├── infrastructure/ # Docker and deployment configs
└── task-log/      # Development task documentation
    ├── completed/ # Completed task logs
    ├── current/   # Current task documentation
    ├── next/      # Upcoming features and tasks
    └── notes/     # Development guidelines
```

## Getting Started

1. Install PNPM if you haven't already:

   ```bash
   corepack enable
   corepack prepare pnpm@8.15.4 --activate
   ```

2. Install dependencies:

   ```bash
   pnpm install
   ```

3. Set up environment variables:

   ```bash
   cp infrastructure/.env.example infrastructure/.env
   ```

4. Start development servers:
   ```bash
   pnpm dev
   ```

## Development

- Use `pnpm build` to build all packages and applications
- Use `pnpm lint` to lint all code
- Use `pnpm test` to run tests
- Use `pnpm clean` to clean all build artifacts

## Monorepo Structure

This project uses PNPM workspaces and Turborepo for monorepo management:

- `apps/*` - Contains standalone applications
  - `backend/` - Django backend with API and chat functionality
  - `frontend/` - Next.js frontend application
- `packages/*` - Contains shared packages
  - `ui/` - Reusable UI components
  - `types/` - Shared TypeScript types
  - `chat-widget/` - Embeddable chat widget
- `infrastructure/*` - Contains Docker and deployment configurations
- `task-log/*` - Development documentation and task tracking

## Task Documentation

All development tasks are tracked in the `task-log` directory:

- `completed/` - Contains logs of completed tasks with implementation details
- `current/` - Documentation for tasks currently in progress
- `next/` - Planned features and upcoming tasks
- `notes/` - Development guidelines and best practices

## Project Status

### Completed Tasks ✅

- Project structure and monorepo setup
- Turborepo and PNPM workspace configuration
- Next.js 15 frontend initialization with TypeScript and TailwindCSS
- Django backend project initialization
- Basic package structure for UI, types, and chat-widget
- Initial Docker compose configuration

### Current Focus 🚧

1. Implementing basic UI components in @repo/ui
2. Setting up shared types in @repo/types
3. Configuring Django REST framework and basic endpoints
4. Starting chat widget development

### To-Do List 📋

#### Frontend

- Create basic layout structure
- Implement authentication pages
- Set up API client configuration
- Implement chat interface
- Add error handling and loading states

#### Backend

- Configure Django REST framework
- Set up authentication system
- Implement API endpoints
- Add database models
- Configure CORS
- Set up WebSocket for chat

#### Packages

- Define shared types (user, chat, API response types)
- Create base UI components (Button, Input, Card, Modal, Form elements)
- Implement chat widget components and logic
- Add component documentation and tests

#### Infrastructure

- Complete Docker service configurations
- Set up CI/CD pipeline
- Configure production deployment
- Set up testing infrastructure (Jest, pytest, Cypress)

#### Documentation

- Create API documentation
- Add package usage documentation
- Create deployment guide
- Add contributing guidelines

## License

Private
