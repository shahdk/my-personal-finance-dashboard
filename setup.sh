#!/bin/bash

# Personal Finance Dashboard Setup Script
# This script sets up the entire application using Docker

set -e  # Exit on any error

echo "🏦 Personal Finance Dashboard Setup"
echo "=================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

# Check if Docker is installed
check_docker() {
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed. Please install Docker first."
        print_info "Visit: https://docs.docker.com/get-docker/"
        exit 1
    fi
    print_status "Docker is installed"
}

# Check if Docker Compose is available
check_docker_compose() {
    if ! docker compose version &> /dev/null; then
        print_error "Docker Compose is not available. Please install Docker Compose."
        exit 1
    fi
    print_status "Docker Compose is available"
}

# Check if Docker daemon is running
check_docker_daemon() {
    if ! docker info &> /dev/null; then
        print_error "Docker daemon is not running. Please start Docker."
        exit 1
    fi
    print_status "Docker daemon is running"
}

# Stop and remove existing containers
cleanup_existing() {
    print_info "Cleaning up existing containers..."
    docker compose down --volumes --remove-orphans 2>/dev/null || true
    print_status "Cleanup completed"
}

# Build and start the application
start_application() {
    print_info "Building and starting the Personal Finance Dashboard..."
    print_info "This may take a few minutes on first run..."
    
    # Build and start containers
    if docker compose up --build -d; then
        print_status "Containers started successfully"
    else
        print_error "Failed to start containers"
        exit 1
    fi
}

# Wait for services to be ready
wait_for_services() {
    print_info "Waiting for services to be ready..."
    
    # Wait for PostgreSQL
    echo -n "Waiting for PostgreSQL to be ready"
    local timeout=60
    local count=0
    while [ $count -lt $timeout ]; do
        if docker compose exec postgres pg_isready -U demo_user -d personal_finance &> /dev/null; then
            echo
            print_status "PostgreSQL is ready"
            break
        fi
        echo -n "."
        sleep 2
        count=$((count + 2))
    done
    
    if [ $count -ge $timeout ]; then
        echo
        print_error "PostgreSQL failed to start within $timeout seconds"
        exit 1
    fi
    
    # Wait for Streamlit app
    echo -n "Waiting for Streamlit app to be ready"
    count=0
    while [ $count -lt $timeout ]; do
        if curl -f http://localhost:8501/_stcore/health &> /dev/null; then
            echo
            print_status "Streamlit app is ready"
            break
        fi
        echo -n "."
        sleep 2
        count=$((count + 2))
    done
    
    if [ $count -ge $timeout ]; then
        echo
        print_warning "Streamlit app may still be starting. Check manually at http://localhost:8501"
    fi
}

# Display final information
show_completion_info() {
    echo
    echo "🎉 Setup Complete!"
    echo "=================="
    echo
    print_status "Personal Finance Dashboard is now running!"
    echo
    print_info "Access the application:"
    echo "  📊 Dashboard: http://localhost:8501"
    echo "  🗄️  Database: localhost:5432"
    echo "     - Database: personal_finance"
    echo "     - Username: demo_user"
    echo "     - Password: demo_password"
    echo
    print_info "Useful commands:"
    echo "  📋 View logs:           docker compose logs -f"
    echo "  🔄 Restart services:    docker compose restart"
    echo "  ⏹️  Stop services:       docker compose down"
    echo "  🗑️  Full cleanup:        docker compose down --volumes --remove-orphans"
    echo
    print_warning "Note: If using Ollama chat assistant, make sure Ollama is running locally"
    print_info "Ollama setup instructions can be found in OLLAMA_CONNECTION.md"
    echo
}

# Check if we're in the right directory
check_directory() {
    if [ ! -f "docker-compose.yml" ]; then
        print_error "docker-compose.yml not found. Please run this script from the project root directory."
        exit 1
    fi
    print_status "Found docker-compose.yml - in correct directory"
}

# Main execution
main() {
    echo
    print_info "Starting setup process..."
    
    check_directory
    check_docker
    check_docker_compose
    check_docker_daemon
    
    cleanup_existing
    start_application
    wait_for_services
    show_completion_info
}

# Run main function
main "$@" 