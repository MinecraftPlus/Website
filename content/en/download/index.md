---
Title: Download
Description: Download page
Author: Wituch

Template: tmpl/index
Language: en
pid: download

Date: 2020-10-10
Order: 3
---

<style>
table {
    width: 100%;
    font-size: 10pt;
}
th, td {
    vertical-align: middle;
}
</style>

Each version of MinecraftPlus works just like the original Minecraft. To run the game you need a Minecraft launcher (any one that supports original `.json` configuration files).

# Downloading the MC + client

To run the game client in the MiecraftPlus edition, you need to download the appropriate version configuration from the list below and then install it.
In case of a download problem, click on the RMB link and select "Save link as...".

<table>
    <colgroup>
        <col style = "width: 35%">
        <col style = "width: auto">
        <col style = "width: 100pt">
        <col style = "width: 70pt">
    </colgroup>
    <thead> <tr> <th> Release name </th> <th> Version </th> <th> Base version * </th> <th> Link </th> </tr> </thead>
    <tbody>
      <tr>
        <td rowspan = "3"> Cannon Update </td>
        <td> 0.0.2 </td> <td rowspan = "4"> 1.15.2 </td>
        <td> <a download href="%assets_url%/downloads/minecraft/minecraftplus-0.0.2.json"> download </a> </td>
      </tr>
      <tr>
        <td> 0.0.1 </td>
        <td> <a download href="%assets_url%/downloads/minecraft/minecraftplus-0.0.1.json"> download </a> </td>
      </tr>
      <tr>
        <td> 0.0.1-SNAPSHOT </td>
        <td> <a download href="%assets_url%/downloads/minecraft/minecraftplus-0.0.1-SNAPSHOT.json"> download </a> </td>
      </tr>
      <tr>
        <td> Zero Update </td>
        <td> 0.0.0 </td>
        <td> <a download href="%assets_url%/downloads/minecraft/minecraftplus-0.0.0.json"> download </a> </td>
      </tr>
      <tr> <td colspan = "4"> * version of the original version of the game whose content is present in the given version of MC + </td> </tr>
    </tbody>
</table>

If you encounter a bug in MinecraftPlus, have ideas to improve or add new functionality, please report it to <a href="https://bitbucket.org/minecraftplus/minecraftplus/issues" target="_blank"> this link. </a>

# MC + client installation

The downloaded configuration file for the `minecraftplus-x.x.x.json` version (or for the transitional versions` minecraftplus-x.x.x-SNAPSHOT.json`) should be placed in a folder with the same name as the file, without the `.json` extension.
The folder with the configuration file contained in it should be moved to the versions folder `.minecraft/versions/` (most often it is `%appdata%/.minecraft/versions/`) used by the used Minecraft launcher.

# Starting the MC + client

To run the game in the MinecraftPlus version, add a new version in the game launcher. To do this, you need to configure a new installation that will use the downloaded configuration of the game version.
Pay attention to the type of downloaded configuration - if the name contains the word `SNAPSHOT`, it is a transitional release and you should unlock the use of transitional versions in the launcher.

# Launching Spigot+

The launch of the SpigotPlus server is analogous to the standard Spigot server.

To run the SpigotPlus server you need to download a ready engine from the list below.
In case of a download problem, click on the RMB link and select "Save link as...".

<table>
    <colgroup>
        <col style = "width: auto">
        <col style = "width: 100pt">
        <col style = "width: 60pt">
        <col style = "width: auto">
        <col style = "width: auto">
        <col style = "width: 70pt">
    </colgroup>
    <thead>
        <tr> <th rowspan = "2"> Version </th> <th colspan = "4"> Compatibility </th> <th rowspan = "2"> Link </th> </tr>
        <tr> <th> Release </th> <th> MC + </th> <th> API </th> <th> Plugins * </th> </tr>
    </thead>
    <tbody>
      <tr>
        <td> 0.0.2 </td>
        <td rowspan = "2"> Cannon Update </td> <td> 0.0.2 </td> <td> 0.0.2 </td> <td rowspan = "3" colspan = "1"> Spigot 1.15. 2 </td>
        <td> <a download href="%assets_url%/downloads/spigotplus/spigotplus-0.0.2.jar"> download </a> </td>
      </tr>
      <tr>
        <td> 0.0.1-SNAPSHOT </td>
        <td> 0.0.1 </td> <td> 0.0.2-SNAPSHOT </td>
        <td> <a download href="%assets_url%/downloads/spigotplus/spigotplus-0.0.1-SNAPSHOT.jar"> download </a> </td>
      </tr>
      <tr>
        <td> 0.0.0 </td>
        <td> Zero Update </td> <td> 0.0.0 </td> <td> 0.0.1 </td>
        <td> <a download href="%assets_url%/downloads/spigotplus/spigotplus-0.0.0.jar"> download </a> </td>
      </tr>
      <tr><td colspan = "6">* plug-in compatibility is provided at API level; plugins or their functionalities beyond the scope of the Spigot+ API may be incompatible with the Spigot+ engine due to its structure different from the original Spigot engine.</td></tr>
    </tbody>
</table>

If you encounter a bug in SpigotPlus, have ideas to improve or add new functionality, please report it to <a href="https://bitbucket.org/minecraftplus/spigotplus/issues" target="_blank">this link.</a>

# Spigot+ API

The API allowing for the integration of plugins with the news brought by the updates will be made available as soon as the project's repository is moved to public access.
If you need API access right now, please contact us on our discord.
