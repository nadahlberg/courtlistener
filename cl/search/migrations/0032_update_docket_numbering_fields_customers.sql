BEGIN;
--
-- Add field federal_defendant_number to docket
--
ALTER TABLE "search_docket" ADD COLUMN "federal_defendant_number" smallint NULL;
--
-- Add field federal_dn_case_type to docket
--
ALTER TABLE "search_docket" ADD COLUMN "federal_dn_case_type" varchar(6) DEFAULT '' NOT NULL;
ALTER TABLE "search_docket" ALTER COLUMN "federal_dn_case_type" DROP DEFAULT;
--
-- Add field federal_dn_judge_initials_assigned to docket
--
ALTER TABLE "search_docket" ADD COLUMN "federal_dn_judge_initials_assigned" varchar(5) DEFAULT '' NOT NULL;
ALTER TABLE "search_docket" ALTER COLUMN "federal_dn_judge_initials_assigned" DROP DEFAULT;
--
-- Add field federal_dn_judge_initials_referred to docket
--
ALTER TABLE "search_docket" ADD COLUMN "federal_dn_judge_initials_referred" varchar(5) DEFAULT '' NOT NULL;
ALTER TABLE "search_docket" ALTER COLUMN "federal_dn_judge_initials_referred" DROP DEFAULT;
--
-- Add field federal_dn_office_code to docket
--
ALTER TABLE "search_docket" ADD COLUMN "federal_dn_office_code" varchar(3) DEFAULT '' NOT NULL;
ALTER TABLE "search_docket" ALTER COLUMN "federal_dn_office_code" DROP DEFAULT;
--
-- Add field parent_docket to docket
--
ALTER TABLE "search_docket" ADD COLUMN "parent_docket_id" integer NULL CONSTRAINT "search_docket_parent_docket_id_1a514426_fk_search_docket_id" REFERENCES "search_docket"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "search_docket_parent_docket_id_1a514426_fk_search_docket_id" IMMEDIATE;
--
-- Create an index on the parent_docket_id column in the search_docket table
--
CREATE INDEX "search_docket_parent_docket_id_1a514426" ON "search_docket" ("parent_docket_id");
COMMIT;