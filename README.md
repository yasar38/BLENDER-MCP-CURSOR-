# BlenderMCP - Blender Model Context Protocol Integration

BlenderMCP connects Blender to Cursor through the Model Context Protocol (MCP), allowing Cursor to directly interact with and control Blender. This integration enables AI-assisted 3D modeling, scene creation, and manipulation through natural language commands.

This project is a modified version of [BlenderMCP](https://github.com/ahujasid/blender-mcp), adapted specifically for Cursor integration.

## Features | Özellikler

- **Two-way communication**: Connect Cursor to Blender through a socket-based server
- **Object manipulation**: Create, modify, and delete 3D objects in Blender
- **Material control**: Apply and modify materials and colors
- **Scene inspection**: Get detailed information about the current Blender scene
- **Code execution**: Run Python code in Blender through Cursor commands

---

# English Installation Guide

## Prerequisites
- Blender 3.0 or newer
- Python 3.10 or newer
- Homebrew (for Mac)
- UV package manager

## Installation Steps

### 1. Install UV Package Manager

**For Mac:**
```bash
brew install uv
```

**For Windows:**
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Install Blender Addon
1. Download `addon.py` file
2. Open Blender
3. Go to Edit > Preferences > Add-ons
4. Click "Install..."
5. Select the `addon.py` file
6. Enable the addon (check the box)

### 3. Install Python Package
Run these commands in terminal:
```bash
# Go to project directory
cd blender-mcp

# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # For Mac/Linux
# or
.venv\Scripts\activate  # For Windows

# Install package
uv pip install -e .
```

### 4. MCP Configuration
1. Create `mcp.json` file in project directory:
```json
{
    "mcpServers": {
        "blender": {
            "command": "/path/to/blender-mcp/.venv/bin/python",
            "args": [
                "-m",
                "blender_mcp.server",
                "--port",
                "9876"
            ]
        }
    }
}
```
Note: Replace `/path/to/` with your actual path.

### 5. Cursor Setup
1. Open Cursor
2. Go to Settings > MCP
3. Click "Add Server"
4. Select your `mcp.json` file

## Usage

### Starting Connection
1. In Blender:
   - Press N to open side panel
   - Find "BlenderMCP" tab
   - Click "Start MCP Server"
   - Check console for "Server started on port 9876"

2. In Cursor:
   - Verify MCP server shows "Connected"

### Example Commands
- "Create a cube in Blender"
- "Add a sphere above the cube"
- "Make the cube red"
- "Rotate the sphere 45 degrees"

## Troubleshooting

1. **"Client closed" Error**
   - Restart Blender
   - Disable and re-enable addon
   - Click "Start MCP Server" again
   - Restart Cursor

2. **Port Conflict**
   - Check if port 9876 is in use
   - Use `lsof -i :9876` to check port
   - Restart Blender if needed

---

# Türkçe Kurulum Rehberi

## Gereksinimler
- Blender 3.0 veya daha yeni sürüm
- Python 3.10 veya daha yeni sürüm
- Homebrew (Mac için)
- UV paket yöneticisi

## Kurulum Adımları

### 1. UV Paket Yöneticisinin Kurulumu

**Mac için:**
```bash
brew install uv
```

**Windows için:**
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Blender Eklentisinin Kurulumu
1. `addon.py` dosyasını indirin
2. Blender'ı açın
3. Edit > Preferences > Add-ons menüsüne gidin
4. "Install..." butonuna tıklayın
5. İndirdiğiniz `addon.py` dosyasını seçin
6. Eklentiyi aktif edin (onay kutusunu işaretleyin)

### 3. Python Paketinin Kurulumu
Terminal'de şu komutları çalıştırın:
```bash
# Proje klasörüne gidin
cd blender-mcp

# Sanal ortam oluşturun
uv venv

# Sanal ortamı aktifleştirin
source .venv/bin/activate  # Mac/Linux için
# veya
.venv\Scripts\activate  # Windows için

# Paketi yükleyin
uv pip install -e .
```

### 4. MCP Yapılandırması
1. Proje klasöründe `mcp.json` dosyası oluşturun:
```json
{
    "mcpServers": {
        "blender": {
            "command": "/path/to/blender-mcp/.venv/bin/python",
            "args": [
                "-m",
                "blender_mcp.server",
                "--port",
                "9876"
            ]
        }
    }
}
```
Not: `/path/to/` kısmını kendi bilgisayarınızdaki gerçek yol ile değiştirin.

### 5. Cursor Ayarları
1. Cursor'u açın
2. Settings > MCP menüsüne gidin
3. "Add Server" butonuna tıklayın
4. Oluşturduğunuz `mcp.json` dosyasını seçin

## Kullanım

### Bağlantıyı Başlatma
1. Blender'da:
   - N tuşuna basarak yan paneli açın
   - "BlenderMCP" sekmesini bulun
   - "Start MCP Server" butonuna tıklayın
   - Konsolda "Server started on port 9876" mesajını görün

2. Cursor'da:
   - MCP sunucusunun "Connected" durumunda olduğunu kontrol edin

### Örnek Komutlar
- "Create a cube in Blender"
- "Add a sphere above the cube"
- "Make the cube red"
- "Rotate the sphere 45 degrees"

## Sorun Giderme

1. **"Client closed" Hatası**
   - Blender'ı yeniden başlatın
   - Eklentiyi devre dışı bırakıp tekrar etkinleştirin
   - "Start MCP Server" butonuna tekrar tıklayın
   - Cursor'u yeniden başlatın

2. **Port Çakışması**
   - 9876 portunun kullanımda olup olmadığını kontrol edin
   - `lsof -i :9876` komutu ile portu kontrol edin
   - Gerekirse Blender'ı yeniden başlatın

## License | Lisans

MIT License

## Contributing | Katkıda Bulunma

Feel free to submit issues and pull requests.
Hata raporları ve öneriler için Issues bölümünü kullanabilirsiniz.
