# Pydantic AI Django Project

A modern AI-powered application built with Django, React, and Pydantic.

## Prerequisites

- Node.js >= 18
- PNPM >= 8.15.4
- Python >= 3.11
- Docker and Docker Compose

## Project Structure

```
src/
├── apps/
│   ├── backend/     # Django backend application
│   └── frontend/    # React frontend application
├── packages/
│   ├── ui/          # Shared UI components
│   ├── types/       # Shared TypeScript types
│   └── chat-widget/ # Chat widget package
└── infrastructure/  # Docker and deployment configs
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

- `src/apps/*` - Contains standalone applications
- `src/packages/*` - Contains shared packages
- `infrastructure/*` - Contains Docker and deployment configurations

## License

Private
