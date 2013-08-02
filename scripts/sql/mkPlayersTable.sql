/*
 * Author: Tim Fox
 *  sql to generate player information. This is mainly used to aggrigate which HBase row keys
 *  are needed for an analysis job
 */

create table players (
    player_id int auto_increment not null,
    name varchar(25) not null,
    clan varchar(25) not null,
    race varchar(7) not null,

    primary key (player_id),
);

create index platerIndex
    on players(
    player_id,
    name,
    race
);

