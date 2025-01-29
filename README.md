
# Supporters Role Cog

A Redbot cog that manages the assignment and removal of a "Supporters" role based on a set of predefined roles. This cog automatically adds or removes the "Supporters" role for users who gain or lose specific supporter roles, and it can notify a specified channel when these changes occur.

## Features

- **Automatic Role Management**: Automatically assigns the "Supporters" role when users gain any of the predefined supporter roles, and removes the "Supporters" role when they lose all the supporter roles.
- **Manual Role Check**: A command to manually check and update the "Supporters" role for all members of the server.
- **Notifications**: Sends a notification to a specified channel when a user gains or loses the "Supporters" role.
- **Periodic Role Check**: Automatically checks and updates the "Supporters" role for all members every 30 minutes.

## Installation

1. Clone or download this repository to your Redbot cogs directory:

   ```bash
   git clone https://github.com/jjjonesjr33/Jones-cogs.git
   ```

2. Install the cog by loading it in your Redbot:

   In Discord, run the following command:

   ```bash
   [p]load supporters
   ```

3. Ensure you have set the channel ID for role change notifications by editing the cog's code. Look for this line and replace `123456789012345678` with the actual channel ID:

   ```python
   self.notification_channel_id = 123456789012345678  # Change this to the channel you want the notifications in
   ```

## Configuration

The cog uses a predefined list of supporter roles. When a user gains any of these roles, the "Supporters" role is automatically assigned. If a user loses all supporter roles, the "Supporters" role is removed. The list of supporter roles is configured in the cog as follows:

```python
self.supporter_roles_ids = [
    1049435358921768960,
    1306140535714746380,
    1330228125421801563,
    1330245591120216086,
    1330253265081860157,
    1330808905181429824,
    1330253044570394634,
    1330252787786973184,
    1330251250255663184,
    1330249471354863700,
    689246700531220535,
    689246700531220532,
    689246700531220525
]
```

### Notification Channel

To receive notifications when users are added or removed from the "Supporters" role, make sure to update the `self.notification_channel_id` with the ID of the channel you want to receive these notifications in. This is where the cog will send a message whenever a role change happens.

## Commands

- **`[p]check_supporters`**: This command manually checks and updates the "Supporters" role for all members in the server. Only admins or users with the "Manage Roles" permission can use this command.

   Example usage:
   ```
   [p]check_supporters
   ```

## Background Tasks

- **Periodic Role Check**: The cog automatically runs a task every 30 minutes to check and update the "Supporters" role for all members across all guilds that the bot is in.

## How It Works

1. **on_member_update Listener**:
   - The cog listens for member updates and checks if a user gains or loses any of the predefined supporter roles. If they gain one of the supporter roles, the "Supporters" role is added. If they lose all supporter roles, the "Supporters" role is removed.
   
2. **Notify Role Changes**:
   - When a user gains or loses the "Supporters" role, the cog sends a notification to the configured channel, indicating which role was added or removed.

3. **Manual and Periodic Role Checks**:
   - The `[p]check_supporters` command can be used to manually trigger a check for all members. Additionally, the cog runs a background task every 30 minutes to ensure all members have the appropriate "Supporters" role based on the supporter roles they possess.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.
