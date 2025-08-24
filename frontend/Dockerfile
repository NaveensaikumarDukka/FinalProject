FROM node:18-alpine

# Accept build arguments
ARG NEXT_PUBLIC_BACKEND_URL
ARG NEXT_PUBLIC_IS_DOCKER
ARG NEXT_PUBLIC_DEV_MODE

# Set environment variables for build time
ENV NEXT_PUBLIC_BACKEND_URL=$NEXT_PUBLIC_BACKEND_URL
ENV NEXT_PUBLIC_IS_DOCKER=$NEXT_PUBLIC_IS_DOCKER
ENV NEXT_PUBLIC_DEV_MODE=$NEXT_PUBLIC_DEV_MODE

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application code
COPY . .

# Build the application
RUN npm run build

# Expose port
EXPOSE 3001

# Start the application
CMD ["npm", "start"] 