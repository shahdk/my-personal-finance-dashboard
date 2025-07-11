# Connecting Docker Container to Local Ollama

> AI-Generated Doc

This guide explains how to connect your containerized Personal Finance Dashboard to Ollama running on your local machine.

## Prerequisites

1. **Install Ollama on your local machine** (not in Docker):
   ```bash
   # On macOS
   brew install ollama
   
   # Or download from https://ollama.com/download
   ```

2. **Start Ollama service** on your local machine:
   ```bash
   ollama serve
   ```

3. **Pull the gemma3n model** (or your preferred model):
   ```bash
   ollama pull gemma3n
   ```

## Connection Methods

### Method 1: Using host.docker.internal (Recommended - Already Configured)

This method is **already configured** in your docker-compose.yml and works best with Docker Desktop.

```yaml
# In docker-compose.yml (already set up)
environment:
  OLLAMA_HOST: host.docker.internal

extra_hosts:
  - "host.docker.internal:host-gateway"
```

**To use this method:**
1. Start Ollama on your local machine: `ollama serve`
2. Run your Docker container: `docker-compose up`
3. The container will automatically connect to your local Ollama

### Method 2: Using your machine's IP address

If `host.docker.internal` doesn't work on your system, you can use your machine's IP:

1. **Find your machine's IP address:**
   ```bash
   # On macOS/Linux
   ifconfig | grep "inet " | grep -v 127.0.0.1
   
   # On Windows
   ipconfig
   ```

2. **Update docker-compose.yml:**
   ```yaml
   environment:
     OLLAMA_HOST: 192.168.1.100  # Replace with your actual IP
   ```

### Method 3: Using host networking (Linux only)

On Linux, you can use host networking mode:

```yaml
# Add to docker-compose.yml app service
network_mode: host
```

## Testing the Connection

Once your containers are running, you can test the Ollama connection:

1. **Check if Ollama is accessible from the container:**
   ```bash
   docker-compose exec app curl http://host.docker.internal:11434/api/version
   ```

2. **Use the Chat Assistant** in your dashboard at http://localhost:8501

3. **Look for connection status** in the Streamlit interface:
   - 🟢 Green: Ollama Connected
   - 🔴 Red: Connection Error

## Troubleshooting

### Connection Issues

1. **Ensure Ollama is running** on your local machine:
   ```bash
   ollama serve
   # Should show: Ollama is running on http://localhost:11434
   ```

2. **Check firewall settings** - ensure port 11434 is accessible

3. **Verify Ollama models** are available:
   ```bash
   ollama list
   ```

4. **Check Docker logs** for connection errors:
   ```bash
   docker-compose logs app
   ```

### Alternative Configuration

If you need to use a different host or port, you can override the environment variable:

```bash
# Set custom Ollama host
OLLAMA_HOST=my-ollama-server.local docker-compose up

# Or edit docker-compose.yml
environment:
  OLLAMA_HOST: my-ollama-server.local:11434
```

## Security Notes

- Ollama will be accessible from your Docker container but remains on your local network
- No external exposure is created by this configuration
- The `extra_hosts` setting only affects container-to-host communication

## Performance Tips

1. **Use a fast model** like `gemma3n` for better response times
2. **Warm up the model** by asking a simple question first
3. **Monitor resource usage** as LLMs can be memory-intensive

Your Personal Finance Dashboard will now be able to use your local Ollama installation for AI-powered financial analysis! 