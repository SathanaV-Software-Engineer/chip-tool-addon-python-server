# CHIP Tool API Add-on for Home Assistant

This Home Assistant add-on exposes the `chip-tool` command-line tool via a simple Flask API.

## Installation

1. In Home Assistant, go to **Settings → Add-ons → Add-on Store**
2. Click the **⋮ menu** (top right) → **Repositories**
3. Add this repository URL:
4. Install the add-on named **CHIP Tool API**
5. Start the add-on, and test by sending an API request to port `6000`

## Example Request

```bash
curl -X POST http://homeassistant.local:6000/run \
-H "Content-Type: application/json" \
-d '{"args": "pairing onnetwork 1234 20202021"}'
